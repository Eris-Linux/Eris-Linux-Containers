# Container Example for Eris Linux - API test TCP

## Description

This project is an example of a container that can be used on the Eris Linux environment.

The embedded application is used to test the Eris API.

The application provides an HMI on TCP port 10000, which can be accessed using any generic TCP client such as `telnet`, `nc`, `putty`, and so on.


This example builds a C-language application based on multiple files and a `Makefile`.
The most interesting point of this example is the use of the `liberis` library to access Eris Linux API.


Note that `liberis` depends on `libcurl`, as can be seen in the `LDLIBS` variable in the `Makefile`.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers package.
For example:

```
$ ./create-container  arm64  ./06-api-test-tcp  api-test-tcp-container
```

After a few minutes, you'll find the container in your build directory:

```
$ ls
  [...]  api-test-tcp-container.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Exported Ports` field with `10000:10000/tcp`.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you can reach the application:

```
$ telnet  <device-ip-address>  10000
```

or

```
$ nc <device-ip-address> 10000
```


For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

