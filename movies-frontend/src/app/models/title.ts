import {Type} from './type';
import {Genre} from './genre';

export class Title {
  tconst: string;
  type: Type;
  primaryTitle: string;
  originalTitle: string;
  isAdult: boolean;
  startYear: Date;
  endYear: Date;
  runtimeMinutes: number;
  genres: Genre[];
}
