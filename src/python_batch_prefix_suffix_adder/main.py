
"""
Description:
  Program takes user input to bulk add a prefix and/or suffix to a file or directory.
"""

import argparse, glob, os, sys
# for pip production
# from .prefix import process
# from .suffix import process
# for development
# from prefix import process
# from suffix import process


def main():
  # default test state
  test = False
  # default prefix value
  prefix = ""
  # default suffix value
  suffix = ""
  # default target type
  target = "file"

  test_help_text = """
    (Optional) Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode].
  """
  prefix_help_text = """
    (Optional) Prefix to add to specified target. Example: `-pf prefix`
  """
  suffix_help_text = """
    (Optional) Suffix to add to specified target. Example: `-sf suffix`
  """
  target_type_help_text = """
    (Required) Declares if program will target all files or folders in working directory.\n
    Example: `-ty file`\n
    Example: `-ty folder`
  """

  args = argparse.ArgumentParser(description="Program takes user input to bulk add a prefix and/or suffix to a file or directory")
  # command line option running program in "test" mode
  args.add_argument(
    "-t",
    "--test",
    type=int,
    help=test_help_text
  )
  # command line option for setting the target string
  args.add_argument(
    "-pf",
    "--prefix",
    type=str,
    help=prefix_help_text
  )
  # command line option for setting new string value
  args.add_argument(
    "-sf",
    "--suffix",
    type=str,
    help=suffix_help_text
  )
  # command line option for specifying file type restriction
  args.add_argument(
    "-ty",
    "--type",
    "-tr",
    "--target",
    type=str,
    help=target_type_help_text
  )
  # gets `args` from command line
  args = args.parse_args()

  print(args)

  # # # processes `args` and returns dictionary
  # arguments = process_args(args)

  # # kills program if an error is found in user input
  # try:
  #   if arguments["error"]:
  #     print(arguments["error"])
  #     sys.exit()
  # except:
  #   pass

  # # Collects all directories in a the current working directory
  # if arguments["target_type"] == "directory":
  #   if args.test:
  #     # will fail if used outside of program folder. Oh well.
  #     directory_location = glob.glob(os.getcwd() + "\\rename")
  #   else:
  #     directory_location = glob.glob(os.getcwd())

  #   # generates list of directories
  #   directories = []
  #   for item in os.listdir(directory_location[0]):
  #     # identifies if given `item` is a directory or not
  #     # print(item + " --> " + str(os.path.isdir(directory_location[0] + "\\" + item)))
  #     if os.path.isdir(directory_location[0] + "\\" + item):
  #       directories.append(item)

  #   # print(directories)

  #   # function to rename each folder/directory matching arguments given
  #   if len(directories) > 0:
  #     rename_directories(arguments, directory_location, directories)

  # # Collects all files in given directory with matching extension
  # else:
  #   # collects list of all files with the desired extention in the specified directory
  #   target_files = glob.glob(arguments["directory"] + "\\*." + arguments["target_type"])

  #   # function to rename each file in `target_files`
  #   if len(target_files) > 0:
  #     rename_files(arguments, target_files)


if __name__ == "__main__":
  main()
