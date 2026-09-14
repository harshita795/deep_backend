# The echo command prints text back out to us

```bash
echo "I use Linux"
```

# Terminal

## Terminal is just a program that lets us issue text-based commands and renders the output of those commands.

# Shell

## The program that runs those commands.

## Shells are often referred to as "REPLs." REPL stands for

- Read
- Eval (evaluate)
- Print
- Loop

## This is a way of saying that shells are programs that:

- Read the commands you type
- Evaluate those commands, usually by running other programs on our computer
- Print the output of those commands
- Give us a new prompt to type another command and repeat

# The expr command evaluates a simple expression and prints the result

```bash
expr 400 - 20
```

# CLI (Command Line Interface)

## A program that allows us to interact with our computer in a text-based way.

# GUI (Graphical User Interface)

## A GUI is the standard visual screen we interact with every day on our computer, phone, or tablet. It represents files and actions using visual shapes.

# Drawbacks of GUIs

- They're weak. You are given much more control over your computer through a CLI. With a GUI you're limited to the options that the developer of the GUI has given you.

- They're slow. Once you know the commands to type, it's much faster to type them than to click through endless menus with a mouse.

- They're not as reproducible. If you want to share a set of instructions, you can just copy and paste commands without worrying about screen sizes and user preferences.

- They're not automatable. It's easy to write code that manipulates text (as you've seen in Python), but it's much harder to write code that manipulates GUIs.

- They're not as cool. You will be invited to 90% fewer romantic outings if you are a GUI user.

# The whoami command is about as simple as commands get: it prints the username of the user you're currently logged in as.

```bash
whoami
```

# Bash and Zsh are shells, and they also happen to be powerful programming languages. They have variables, functions, loops, and more.

## Creating Variables

```bash
name="Lane"
```

## Using a Variable

```bash
echo $name
```

# history command to see the commands we've typed in the past.

```bash
history
```

# Arrow keys

The ↑ arrow goes back in your history, and the ↓ arrow goes forward.

# Clear command clear the terminal screen without deleting the history.

```bash
clear or Ctrl+L
```