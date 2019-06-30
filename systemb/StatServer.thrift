namespace py StatServer

typedef i32 int
struct StatStruct {
	1: double mean,
	2: i32 median,
	3: double variance,
	4: double stddev
}
service StatServer {

	bool ping(),
	StatStruct calculateStat(1: list<int> allNumbers),
	list<int> generateNums();

}
