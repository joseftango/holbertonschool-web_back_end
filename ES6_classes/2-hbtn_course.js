export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  set length(newLength) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  set students(newStudents) {
    if (!Array.isArray()) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = newStudents;
  }
}
