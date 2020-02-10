#!/usr/bin/node
exports.converter = function (base) {
  return function (sosa) {
    return sosa.toString(base);
  };
};
