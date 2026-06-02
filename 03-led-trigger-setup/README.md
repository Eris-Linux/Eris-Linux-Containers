# Container Example for Eris Linux - LED trigger setup.

## Description

This project is an example of a container that can be used on the Eris Linux environment.

It is an example of LED access through LED triggers.

The container will need `/sys/` access privileges.


The main purpose of this container is to demonstrate how simple application code (even a shell script)
can access system resources (the LEDs) using the `/sys/` directory tree, provided that the container
has elevated privileges.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers repository.
For example:

```
$ ./create-container  arm64  ./03-led-trigger-setup  led-trigger-setup-container
```

After a few minutes, you'll find the container in your build directory:

```
$ ls
  [...]  led-trigger-setup-container.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Privileged container` field must be checked in order to access the `/sys/` directory.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you'll see the LEDs periodically switch between most common LED triggers.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

