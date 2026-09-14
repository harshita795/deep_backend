# The pwd command prints our current working directory.

```bash
pwd
```

# The ls ("list") command prints the contents of a directory.

```bash
ls
```

# The cd command "changes directory" to move into a directory.

```bash
cd
```

# Move back out of the current directory.

```bash
cd ..
```

# Absolute Path

## A complete file address starting from the root directory (/) of the computer.

```bash
/home/ryan/passwords/secret.txt
```

# Relative Path

## A partial path that points to a file starting from your current working folder.

```bash
passwords/secret.txt
```

### (This only works if your terminal is already opened inside the /home/ryan folder).

# Print the contents of a file to the terminal

```bash
cat file1.txt
```

# Concatenate the contents of multiple files and print them to the terminal

```bash
cat file1.txt file2.txt
```

# Tab command is used to autocomplete file and folder names

```bash
ls w
```

press Tab

# ls worldbanc/

# The head command prints the first n lines of a file. The -n flag specifies n as shown:

```bash
head -n 10 file1.txt
```

# The tail command prints the last n lines of a file. The -n flag specifies n as shown:

```bash
tail -n 10 file1.txt
```

# The more and less commands let us view the contents of a file, one page (or line) at a time.

## less and more are interactive pagers: they take over our terminal window so we can scroll through a file a page at a time. In less:

- Press the spacebar to move down one page
- Press b to move up one page
- Press / to search
- Press q to quit back to your shell prompt

# Touch

## The touch command updates the access and modification timestamps of a file. By default, if the specified file does not exist, touch will create an empty file with the given filename. Because of this side-effect, we'll often see this command used to quickly create new empty files.

```bash
touch new_file.txt
```

## We can also create multiple files at once by listing them:

```bash
touch some_file.txt some_other_file.txt
```

# The "make directory" command creates a new directory inside (or relative to) the current directory.

```bash
mkdir my_directory
```

# Move

## The move command moves a file or directory from one location to another. We can use it to rename a file or to move it to a different directory altogether. If we're moving a directory, it can't be our current working directory.

### Moving a file from the current directory to another nested directory:

```bash
mv report.csv archives/report.csv
```

### Renaming a file:

```bash
mv draft.md final.md
```

### Moving a file from the current directory, to the parent directory:

```bash
mv invoice.pdf ../invoice.pdf
```

### If we don't want to rename the file and we're just moving it to a different directory, we can omit the filename:

```bash
mv photo.png images/
```

## The remove command deletes a file or empty directory:

```bash
rm some_file.txt
```

## We can optionally add a -r flag to tell the rm command to delete a directory and all of its contents recursively.

```bash
rm -r some_directory
```

## The copy command does what we would (hopefully) expect: it copies a file from one location to another.

```bash
cp source_file.txt destination/
```

## We can also copy a directory and all of its contents recursively by adding the -R flag:

```bash
cp -R my_dir new_dir
```

## The $HOME environment variable contains the absolute path to our home directory:

```bash
echo $HOME
```

## The ~ character is an alias for our home directory

```bash
cd ~
```

## The grep command allows us to search for text in files.

```bash
grep "hello" words.txt
```

### This will print out every line in words.txt that contains the word hello. It's a case-sensitive search, so it will only match hello, not Hello or HELLO

## We can also search multiple files at once

```bash
grep "hello" hello.txt hello2.txt
```

## Recursive Search - We can also search an entire directory, including all subdirectories

```bash
grep -r "hello" .
```

### The . is a special alias for the current directory.

## The find command is a tool for finding files and directories by name, not by their contents.

### Find a File by Name - If we're looking for a file named hello.txt somewhere in our home directory. We can use the find command to search for exactly that title:

```bash
find some_directory -name hello.txt
```

### Pattern Search - The find command can also search for files that match a pattern. For example, if we wanted to find all files that end in .txt, we could run:

```bash
find some_directory -name "*.txt"
```

### Find all filenames that contain the word "chad"

```bash
find some_directory -name "*chad*"
```