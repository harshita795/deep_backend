##  The "help" option prints information about how to use the tool.

- --help (flag)
- -h (flag)
- help (first positional argument)
```bash
grep --help
```

## Flags are options that we can pass to a command to change its behavior.

### The ls command can take a -l flag to show a "long" listing of files.
```bash
ls -l
```

### The -a flag to show "all" files, including hidden files.
```bash
ls -a
```

### Combining all flags
```bash
ls -al
```

## Positional Arguments
- In a shell, commands (programs) can also take arguments. For example, the cd command takes a single argument (the directory to change to):
```bash
cd /home/wagslane
```

- Other commands might take multiple arguments. For example, the mv command takes two arguments: the file to move, and the destination to move it to:
```bash
mv file.txt dest/file.txt
```

## Exit Codes
- 0 is the exit code for success. Any other exit code is an error. 9 times out of 10, if a non-zero exit code is returned (meaning an error) it will be 1, which is the "catch-all" error code.

### Printing Exit Codes
- In a shell, we can access the exit code of the last program we ran with the question mark variable ($?):
```bash
cat greeting.txt
# General Kenobi!
echo $?
# 0
```

```bash
cat file/that/does/not/exist.txt
echo $?
# 1
```

### Running Commands Conditionally
- We can run multiple commands on a single line by separating them with a semicolon (;):
```bash
command1 ; command2
```

- If we only want the second command to run when the first command succeeds (exit code 0), use &&:
```bash
command1 && command2
```

## Standard Output
- It usually called "standard out" or stdout, is the default place where programs print their output. It's just a stream of data that prints to our terminal.

## Standard Error
- It usually called stderr, is a data stream just like standard output, but is intended to be used for error messages.

## Redirecting Streams
- We can redirect stdout and stderr to different places using the > and 2> operators. > redirects stdout, and 2> redirects stderr.

### Redirect stdout to a File
```bash
echo "Hello world" > hello.txt
cat hello.txt
# Hello world
```

### Redirect stderr to a File
```bash
cat doesnotexist.txt 2> error.txt
cat error.txt
# cat: doesnotexist.txt: No such file or directory
```
- In this example, cat is used to intentionally generate an error message (since the file doesn't exist), which is then redirected to error.txt.

## Standard Input
- It usually called "standard in" or stdin, is the default place where programs read their input. It's just a stream of data that programs can read from as they run.

### Redirecting Input
- The < operator redirects a file into a program's stdin. For example, to feed the contents of a file called input.txt into the "word count" program, we can run:
```bash
wc < input.txt
```

- This is not the same as:
```bash
wc input.txt
```
- In wc input.txt, the wc program is accepting a filepath string as an argument, and it opens the file itself.

- In wc < input.txt, the wc program doesn't know anything about the file, the file's contents are just being sent to the program's stdin, and it reads from there.

## Piping
- The pipe operator is |.
- The pipe operator takes the stdout of the program on the left and "pipes" it into the stdin of the program on the right.
```bash
echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
# 10
```

## Unix Philosophy
- The Unix Philosophy is a simple set of principles that have guided the development of Unix-like operating systems for decades. It can be summarized as:

- Write programs that do one thing and do it well.
- Write programs to work together.
- Write programs to handle text streams, because that is a universal interface.

