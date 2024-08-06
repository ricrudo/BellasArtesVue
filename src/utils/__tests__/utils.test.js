import { describe, it, expect } from 'vitest';
import {addElement} from '@/utils/utils.js'

describe('utils.js', () => {

  describe('addElement', () => {
    it('should add a new element with incremented key', () => {
      const obj = { 1: {id_name:'keyword', a: 'value' } };
      addElement(obj, 'keyword');
      expect(obj).toHaveProperty('2');
      expect(obj[2]).toEqual({ id_name:'keyword_2', a: null });
    });

    it('should clean valores anidados', () => {
      const obj = { 1: {id_name:'keyword_1', a: 'value', b:{1:'12', b:4}, c :[1,2,3] } };
      addElement(obj, 'keyword');
      expect(obj).toHaveProperty('2');
      expect(obj[2]).toEqual({id_name:'keyword_2', a: null, b:{1:null, b:null}, c :null });
    });


    it('should handle an empty object correctly', () => {
      const obj = {};
      addElement(obj, 'keyword');
      expect(obj).toEqual({});
    });
  });
});
