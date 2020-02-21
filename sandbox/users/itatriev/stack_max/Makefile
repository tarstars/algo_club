all: StackkTest.class Stackk.class
	java  -cp .:/usr/share/junit-4/lib/junit.jar:/usr/share/hamcrest-core-1.3/lib/hamcrest-core.jar org.junit.runner.JUnitCore StackkTest

StackkTest.class: StackkTest.java
	javac -cp .:/usr/share/junit-4/lib/junit.jar StackkTest.java

Stackk.class: Stackk.java
	javac Stackk.java

