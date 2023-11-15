# postman doc generator

Takes a postman collection and flatten it, so it can be used by [postmanerator](https://github.com/aubm/postmanerator),
addressing [this issue](https://github.com/aubm/postmanerator/issues/72). postmanerator currently only supports single
nested directories. (collection > folder > request)

## Installation

Download the script and install postmanerator, see [postmanerator](https://github.com/aubm/postmanerator#installation).

## Usage

Step 1: Export your postman collection.
Step 2: Run the script.
Step 3: Fill in path.

the script will now flatten your json and use it as input for postmanerator.
Works only for single nested directory.

(collection > folder > folder > request)