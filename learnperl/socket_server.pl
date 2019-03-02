#!/usr/bin/perl
# Filename: server.pl

use strict;
use Socket;

# use port 7890 as default
my $port = shift || 7890;
my $proto = getprotobyname('tcp');
my $server = "192.168.1.2";    # Host IP running the server

# create a socket, make it reusable
socket(SOCKET, PF_INET, SOCK_STREAM, $proto) or die "Can't open socket $!\n";
setsockopt(SOCKET, SOL_SOCKET, SO_REUSEADDR, 1) or die "Can't set socket option to SO_REUSEADDR $!\n";

# bind to a port, then listen
bind(SOCKET, pack_sockaddr_in($port, inet_aton($server))) or die "Can't bind to port $port! \n";

listen(SOCKET, 5) or die "listen: $!\n";

# open(DATA, "<import.txt") or die "Can't open data";
# my @lines = <DATA>;

# accepting a connection
my $client_addr;
while ($client_addr = accept(NEW_SOCKET, SOCKET)) {
	my @lines;
	# send them a message, close connection
	my $name = gethostbyaddr($client_addr, AF_INET);
	#	print NEW_SOCKET "@lines\n";
	print "Connection received from $name\n";
	while(@lines = <NEW_SOCKET>)
	{
		print "@lines\n";
	}

	close NEW_SOCKET;
}
