fun minSelectionSort(arr: IntArray) {
    for (i in 0..arr.lastIndex-1) {
        var minIndex = i
        for (j in i+1..arr.lastIndex) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j
            }
        }

        arr[i] = arr[minIndex].also { arr[minIndex] = arr[i] }
    }
}

fun main() {
    val arr = IntArray(10) { it }.also { it.shuffle() }
    // minSelectionSort(arr)
    println(arr.contentToString())
}