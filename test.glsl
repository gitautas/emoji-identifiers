#version 300 es
precision highp float;
out vec4 res;
uniform sampler2D noise;

void main() {
  int 🪟 = 2;
  res = texelFetch(noise, ivec2(0), 🪟) + 1.0;
}

