# Container Example for Eris Linux - API test with web HMI.

## Description

This directory contains the files needed to build a container image that can run on the Eris Linux environment.

It is an example of an embedded HTTP server and a Web HMI to communicate with the system using the Eris API.


This example is particularly useful for demonstrating how to install a system utility with custom configuration and data files.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers repository.
For example:

```
$ ./create-container  arm64  ./02-api-test-web  api-test-web-container
```

After a few minutes, you'll find the container in your build directory:

```
$ ls
  [...]  api-test-web-container.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container,
- The `Exported Ports` field with `80:80/tcp`.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, fire a web browser and connect to the IP address of the device.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

