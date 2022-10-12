# log-installed-software

Script to easily save the version of the software packages installed on a system.

## Installation and Usage

You can clone the repo with git:

```bash
git clone https://github.com/ami-iit/log-installed-software
```

Then, you can invoke the script in any directory:
~~~
python ./log-installed-software/src/log.py
~~~

After running, the script will create a `installed_software.txt` file that contains a report on the software installed in the system.

If you want to invoke the script in one step and you have `curl` on your machine, and you are 100% sure that you trust the `ami-iit` GitHub organization, you can just run:
~~~
curl -fsSL https://raw.githubusercontent.com/ami-iit/log-installed-software/main/src/log.py | python
~~~

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause/)
