#!/usr/bin/node
exports.callMeMoby = function (numb, funct) {
  for (let i = 0; i < numb; i++) {
    funct();
  }
};
