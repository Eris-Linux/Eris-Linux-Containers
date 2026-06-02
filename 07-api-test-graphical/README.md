# Container Example for Eris Linux - API test using graphical HMI.

## Description

This project is an example of a container that can be used on the Eris Linux environment.

The embedded application is used to test Eris Linux API using a graphical HMI based on the Qt library.


This example builds a C++-language application based on multiple files and a `Makefile`.
The application uses the `liberis` library to access Eris Linux API.


The most important point is the use of the graphical library Qt to propose an interactive HMI.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers package.
For example:

```
$ ./create-container  arm64  ./07-api-test-graphical  api-test-graphical
```

After a few minutes, you'll find the container image in your build directory:

```
$ ls
  [...]  api-test-graphical.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Use graphical display` checkbox must be checked.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you'll see the HMI on the graphical display of the device.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

