# newpaper
This little python script sets up a directory to serve as a new LaTeX document.
All it does is write a `main.tex` file with with a preamble that contains 
the packages that I am used to as well at a custom `\note` command for 
author notes during writing.

The script takes one required command line argument `projpath` that is the path
to the directory you would like created. There are two optional arguments,
`-t` or `--title` which is simply passed as the title inserted into `main.tex`
as well as `-a` or `--author` which is inserted as author of the paper.

## Example

The simplest usage is passing just the project directory path and nothing else

```
> newpaper.py testpaper
```

```
> newpaper.py testpaper -a godzilla-but-nicer -t A Script For LaTeX Projects
```
