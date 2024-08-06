function getHighestKey(myObject) {
  let maxID = 0;
  Object.keys(myObject).forEach(key => {
    const numberID = Number(key);
    if (numberID > maxID) {
      maxID = numberID;
    }
  });
  return maxID > 0 ? maxID : null;
}

function checkType(variable) {
  if (typeof variable === 'number') {
    return 'Number';
  } else if (typeof variable === 'string') {
    return 'String';
  } else if (Array.isArray(variable)) {
    return 'Array';
  } else if (variable instanceof Date) {
    return 'Date';
  } else if (variable === null) {
    return 'null';
  } else {
    return 'Other';
  }
}

function cleanValues(value) {
  const type = checkType(value);

  if (type === 'Other') {
    // Si es un objeto, recorrerlo recursivamente
    if (typeof value === 'object' && value !== null) {
      const cleaned = {};
      Object.keys(value).forEach(key => {
        cleaned[key] = cleanValues(value[key]);
      });
      return cleaned;
    }
    // Si es un array, recorrerlo recursivamente
    if (Array.isArray(value)) {
      return value.map(cleanValues);
    }
  }

  // Para otros tipos de valor, simplemente devuelve null
  return null;
}

export function addElement(myObject, keyword) {
	const highestKey = getHighestKey(myObject);
  if (highestKey !== null) {
    const newKey = highestKey + 1
    const deepCopy = JSON.parse(JSON.stringify(myObject[highestKey]));
    Object.keys(deepCopy).forEach(key => {
      deepCopy[key] = cleanValues(deepCopy[key]);
    });
    deepCopy['id_name'] = keyword + '_' + newKey.toString();
    myObject[newKey] = deepCopy;
  };
}
