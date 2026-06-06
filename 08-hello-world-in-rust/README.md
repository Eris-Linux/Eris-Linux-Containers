# Container Example for Eris Linux - Hello World in Rust

## Description

This project is an example of a container that can be used on the Eris Linux environment.

In the container there is a simple "Hello World!" program written in Rust

The "Hello World" message is written on the standard output of the program, and displayed
on an HTML page reachable via `http://<device-ip>:3000`.


This directory is mostly interesting as an example of how to build a Rust program for Eris Linux container.


## License

This container example is licensed under the MIT license.


## Author

Alexandre GROSSET 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers repository.
For example:

```
$ ./create-container  arm64  ./08-hello-world-in-rust  hello-world-rust
```

After a few minutes, you'll find the container in your build directory:

```
$ ls
  [...]  hello-world-rust.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the `Compatible board` field with the type of board on which you'll use the container.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you can see on the device console:

```
Hello, World! (from Rust)
Hello, World! (from Rust)
Hello, World! (from Rust)
[...]
```

A new line is displayed every 5 seconds.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

