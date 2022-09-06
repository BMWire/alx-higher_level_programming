#!/usr/bin/node
'use strict';

const args = process.argv[2];
if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
