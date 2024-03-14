fun main() {
    val a = Array(20){it}

    a.shuffle()

    println(a.joinToString(", "))

    for (p in a.indices.last downTo 1) {
        for (q in 1..p) {
            if (a[q-1] > a[q]) {
                a[q] = a[q - 1].also {a[q - 1] = a[q]}
            }
        }
    }

    println(a.joinToString(", "))

}
