fun main() {
    val a = Array(20) {it}
    a.shuffle()

    println(a.joinToString(", "))

    for (p in 0 .. a.indices.last - 1) {
        var min_ind = p
        for (q in p + 1 .. a.indices.last) {
            if (a[min_ind] > a[q]) {
                min_ind = q
            }
        }
        a[p] = a[min_ind].also {a[min_ind] = a[p]}
    }

    println(a.joinToString(", "))
}
