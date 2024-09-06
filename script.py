import json
import sys
import os


def get_followers_and_following(followers_file_path, following_file_path):
    followers = [
        o["string_list_data"][0]["value"] for o in json.load(open(followers_file_path))
    ]
    following = [
        o["string_list_data"][0]["value"]
        for o in json.load(open(following_file_path))["relationships_following"]
    ]

    return followers, following


def get_following_but_not_follower(followers, following):
    return list(set(following) - set(followers))


def main():
    if len(sys.argv) == 3:
        followers_file_path, following_file_path = sys.argv[1:]
    elif len(sys.argv) == 2:
        followers_file_path, following_file_path = [
            os.path.join(sys.argv[1], fname)
            for fname in ["followers_1.json", "following.json"]
        ]
    else:
        assert False, "Wrong usage!"

    followers, following = get_followers_and_following(
        followers_file_path, following_file_path
    )

    following_but_not_follower = get_following_but_not_follower(followers, following)

    print(*following_but_not_follower, sep="\n")


if __name__ == "__main__":
    main()
