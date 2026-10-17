export default [
  {
    input: 'src/index.js',
    output: {
      file: 'dist/index.cjs',
      format: 'cjs',
      exports: 'named',
      sourcemap: true,
    },
  },
  {
    input: 'src/index.js',
    output: {
      file: 'dist/index.mjs',
      format: 'esm',
      sourcemap: true,
    },
  },
];
