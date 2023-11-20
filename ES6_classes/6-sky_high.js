import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (this._sqft !== 'number') {
      throw new TypeError('newSqft must be a number');
    }
    this._sqft = newSqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloores) {
    if (newFloores !== 'number') {
      throw new TypeError('newFloores must be a number');
    }
    this._floors = newFloores;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
