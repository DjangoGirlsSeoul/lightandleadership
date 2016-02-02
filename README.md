<h1>Light and Leadership Non-profit Project</h1>

<h3>About</h3>
<p>Django girls Seoul members has gotten an opportunity to contribute to a non-profit project. We will use Python and Django for backend and bootstrap for front end.</h3>

<h3>Setting up your local environment</h3>
-----

<p>This assumes that you have python3 installed. (we are using 3.4 but this should work for most python 3 versions)
Go to a folder where you'll want to save the project folder. </p>

1. Clone the project by entering `git clone git@github.com:rachellcalhoun/lightandleadership.git` in the terminal
    - This will create a folder called `lightandleadership` where you ran the command
    - 'cd ..' to leave this folder

2. Create a virtualenv by creating a new folder `mkdir virtualenvironments` and going into that folder `cd virtualenvironments` 

3. Create the virtual environment <strong> not inside the lightandleadership folder</strong> (mostly copied from the django girls tutorial - check folder names! )
    > ## Virtual environment

    > Before we install Django we will get you to install an extremely useful tool to help keep your coding environment tidy on your computer. It's possible to skip this step, but it's highly recommended. Starting with the best possible setup will save you a lot of trouble in the future!

    > So, let's create a **virtual environment** (also called a *virtualenv*). Virtualenv will isolate your Python/Django setup on a per-project basis. This means that any changes you make to one website won't affect any others you're also developing. Neat, right?
> All you need to do is find a directory in which you want to create the `virtualenv`; your home directory, for example. On Windows it might look like `C:\Users\Name\` (where `Name` is the name of your login).

    > We will make a virtualenv called `myvenv`. The general command will be in the format:

        python3 -m venv myvenv

    > ### Windows

    > To create a new `virtualenv`, you need to open the console (we told you about that a few chapters ago - remember?) and run `C:\Python34\python -m venv myvenv`. It will look like this:

        C:\Users\Name\virtualenvironments> C:\Python34\python -m venv myvenv

    > where `C:\Python34\python` is the directory in which you previously installed Python and `myvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces, accents or special characters. It is also good idea to keep the name short - you'll be referencing it a lot!

    > ### Linux and OS X

    > Creating a `virtualenv` on both Linux and OS X is as simple as running `python3 -m venv myvenv`.
    It will look like this:

        ~/virtualenvironments$ python3 -m venv myvenv

    > `myvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short as you'll be referencing it a lot!

    > > __NOTE:__ Initiating the virtual environment on Ubuntu 14.04 like this currently gives the following error:

    > >     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

    > > To get around this, use the `virtualenv` command instead.

    > >     ~/virtualenvironments$ sudo apt-get install python-virtualenv
    > >    ~/virtualenvironments$ virtualenv --python=python3.4 myvenv

4. Activate the virtualenv (also copied from the djangogirls tutorial - check folder names!)
    > ## Working with virtualenv

    > The command above will create a directory called `myvenv` (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files). 

    > #### Windows 

    > Start your virtual environment by running:

        C:\Users\Name\virtualenvironments> myvenv\Scripts\activate

    > #### Linux and OS X 

    > Start your virtual environment by running:

        ~/virtualenvironments$ source myvenv/bin/activate

    > Remember to replace `myvenv` with your chosen `virtualenv` name!

    > > __NOTE:__ sometimes `source` might not be available. In those cases try doing this instead:

    > >    ~/virtualenvironments$ . myvenv/bin/activate

    > You will know that you have `virtualenv` started when you see that the prompt in your console looks like:

        (myvenv) C:\Users\Name\virtualenvironments>

    > or:

        (myvenv) ~/virtualenvironments$

    > Notice the prefix `(myvenv)` appears!

    > When working within a virtual environment, `python` will automatically refer to the correct version so you can use `python` instead of `python3`.

    > OK, we have all important dependencies in place. We can finally install Django!
    

5. ( 'cd ..' to leave virtualenvironments folder) Go into the `lightandleadership` directory `cd ../lightandleadership`

6. Run `pip install -r requirements.txt` to install the pip dependencies

7. Run `python manage.py runserver`

8. Success! (hopefully)

* If you see anything wrong here, please make an issue or a pull request!



---

We are mostly following the standard [github flow](https://guides.github.com/introduction/flow/). Only difference is that we do not test our PRs in production, but that might change later.

We also have an automatic deploy triggered by travis which puts our code up on python anywhere, which is where our app is hosted.

If you want to read more about how our releases work [here](releases.md)
