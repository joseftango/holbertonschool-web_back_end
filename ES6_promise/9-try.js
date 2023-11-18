export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue[0] = mathFunction();
  } catch (e) {
    queue[0] = e.toString();
  }
  queue[1] = 'Guardrail was processed';
  return queue;
}
