# Container Example for Eris Linux - SSH server

## Description

This directory contains the files needed to build a container image that can run on the Eris Linux environment.

It is an example of a SSH server installation.

Two default accounts are provided in the `Dockerfile`:

- `root` which uses the password `root`
- `eris` which uses the password `linux`

*IMPORTANT*: do not use these passwords on production systems!


This example is particularly useful for understanding the process of creating a container that can then be deployed on systems running Eris Linux.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers repository.
For example:

```
$ ./create-container  arm64  ./01-ssh-server  ssh-server
```

After a few seconds, you'll find the container image in your build directory:

```
$ ls
  [...]  ssh-server.tar.bz2 [...]
```

Connect to your account, or create one, on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.
You will need to re-enter the password when you would upload the container on your devices.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Exported Ports` field with `<external>:22/tcp`, with `<external>` being the external port on which the container will be reachable.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, use:

```
$ ssh  -p <external>  eris@<ip address>
```

With `<ip address>` being the address on wich the device is reachable on the local subnet.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

