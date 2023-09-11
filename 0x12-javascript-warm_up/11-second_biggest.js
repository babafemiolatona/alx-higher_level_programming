#!/usr/bin/node
const args = process.argv;

if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  let max = Math.max.apply(null, args.slice(2));
  const index = args.indexOf(max.toString());
  args.splice(index, 1);
  max = Math.max.apply(null, args.slice(2));
  console.log(max);
}
