export default function getListStudentIds(arr) {
  if (Array.isArray(arr) !== true) {
    return [];
  }
  return arr.map((obj) => obj.id);
}
