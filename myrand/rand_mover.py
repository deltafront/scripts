from os.path import join
from shutil import move
from os import listdir
import datetime

__author__ = 'charlie'
from random import randint

source_dir = "/Users/charlie/Desktop/Sorted playlists/MIne/"
target_dir = "/Users/charlie/Desktop/Sorted playlists/Drop of of Twelves"


def main():
    source_files = get_dir_contents()
    source_dir_length = len(source_files)
    upper_limit = get_upper_limit(source_dir_length)
    random_numbers = get_random_array(upper_limit, source_dir_length)
    random_files = get_random_files(source_files, random_numbers)
    move_files(random_files)


def get_upper_limit(source_files_length):
    now = datetime.datetime.now()
    week_of_year = now.isocalendar()[1]
    weeks_remaining = 54 - week_of_year
    upper = source_files_length / weeks_remaining
    print("Week of year:\t%s\nWeeks remaining:\t%s\nUpper limit:\t%s"
          % (str(week_of_year), str(weeks_remaining), str(upper)))
    return upper


def get_random_array(number_of_files, source_dir_length):
    randoms = []
    for i in range(0, number_of_files):
        random_number = randint(0, source_dir_length)
        while random_number in randoms:
            random_number = randint(0, source_dir_length)
        randoms.append(random_number)
        print("Returning %s files" % len(randoms))
    return randoms


def get_dir_contents():
    return listdir(source_dir)


def get_random_files(files, numbers):
    return [files[n] for n in numbers]


def move_files(random_files):
    for f in random_files:
        source = join(source_dir, f)
        destination = join(target_dir, f)
        print("Moving '%s' to '%s'." % (source, destination))
        move(source, destination)


if __name__ == "__main__":
    main()
