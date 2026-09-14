## Compiled Programs

- A compiled program is a program that has been converted from human-readable source code into machine code (binary). Machine code is a set of instructions that a computer can execute directly: your computer's CPU is hardware that's been designed to execute machine code.

- Programming languages like Go, C, and Rust produce compiled programs.

## Interpreted Programs

- An interpreted program is a program that is executed by another program. The program that executes the interpreted program is called an interpreter. The interpreter reads the source code of the interpreted program and executes it.

- Programming languages like Python, Ruby, and JavaScript, are typically interpreted as they run, which means your computer needs to have the interpreter installed to run the program.

## The which Command

- The which command tells us the location of an installed command line program.

## A shebang (#!) 

- It is a special code line placed at the absolute top of a script that tells the operating system which interpreter program (like /usr/bin/python3 or /bin/sh) to use to automatically execute that file.

- eg- #!/usr/bin/python3

## Excutables

- We use ./ (current directory alias) before a file name to force the terminal to execute a local file rather than looking for an installed system command.

- For example: typing ./script.sh instead of just script.sh.

## Bourne Shell

- sh: The Bourne shell. This is the original Unix shell and is POSIX-compliant. It's very basic and doesn't have many quality-of-life features.
 
- bash: The Bourne Again shell. This is the most popular shell on Linux. It builds on sh, but also has a lot of extra features.

- zsh: The Z shell. This is the most popular shell on macOS. Like bash, it does what sh can do, but also has a lot of extra features.

## Environment Variables

- We can view all of the environment variables that are currently set in our shell with the env command.

- The export command shares a variable with any application launched from our terminal, but it evaporates from memory as soon as we close that specific terminal window
```bash
export NAME="Lane"
```

- We can use the unset command to remove an environment variable from our current shell session:
```bash
unset NAME
```

## PATH

- The PATH environment variable is a colon-separated list of system folders (like /bin:/usr/bin) where the shell automatically searches for an executable program when we type a command, allowing us to simply type ls instead of its full absolute address /bin/ls
```bash
echo $PATH
```

## Changing the Path

- To add a directory to your PATH without overwriting all of the existing directories, use the export command and reference the existing PATH variable:
```bash
export PATH="$PATH:/some/new/directory"
```