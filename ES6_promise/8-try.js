export default function divideFunction(numerator = 0, denominator = 0) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return (numerator / denominator);
}
