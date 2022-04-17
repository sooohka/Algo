function isMonotonic(array) {
  if (array.length < 2) return true
  let status = "unknown" // "unknown", "increasing", "decreasing"
  for (let i = 1; i < array.length; i += 1) {
    if (status === "unknown") {
      if (array[i - 1] < array[i]) status = "increasing"
      else if (array[i - 1] > array[i]) status = "decreasing"
    }
    if (status === "decreasing" && array[i - 1] < array[i]) return false
    if (status === "increasing" && array[i - 1] > array[i]) return false
  }
  return true
}
