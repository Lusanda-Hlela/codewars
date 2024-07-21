function loopArr(arr, direction, steps) {
  // validations
  
  if (!Array.isArray(arr)) {
    throw new Error("Please provide an array.");
  }
  
  if (direction !== "left" && direction !== "right") {
    throw new Error("Direction must either be 'right' or 'left'");
  }
  
  if (typeof steps !== "number" || steps < 0) {
    throw new Error("Steps must be a positive integer.");
  }
  
  const len = arr.length;
  if (steps > len) {
    throw new Error("Number of steps cannot be greater than the size of the array.");
  }
  
  // Left: remove from start; add to the end
  // Right: remove from end; add to the start
  
  if (direction === "left") {
    const shiftedElements = arr.splice(0, steps);
    return arr.concat(shiftedElements);
  } else if (direction === "right") {
    const shiftedElements = arr.splice(len - steps, steps);
    return shiftedElements.concat(arr);
  }
}