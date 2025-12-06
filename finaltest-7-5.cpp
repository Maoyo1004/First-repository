#include<iostream>
#include<vector>
using namespace std ;

int main() {
	int n ;
	cin >> n ;
	vector<int> line( n ) ;
	for ( int i = 0 ; i < n ; ++i ) {
		line[ i ] = i + 1 ;
	}
	int rec = 0 ;
	while ( line.size() > 1 ) {
	    int rem = ( rec + 2 )%line.size() ;
		line.erase( line.begin() + ( rec + 2 )%line.size() ) ;
		rec =  rem%line.size() ;
	}
	cout << line[ 0 ] << "\n" ;
}