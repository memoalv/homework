use Text::CSV;

use strict;
use warnings;

# read csv
my $csv = Text::CSV->new({ sep_char => ',' });
open(my $fileData, '<', 'movies.csv') or die "Could not open movies.csv $!\n";
while(my $line = <$fileData>) {
    chomp $line;

    if ($csv->parse($line)) {
     
          my @fields = $csv->fields();
          
          my $field = $fields[0];

          print $field;
     
      } else {
          warn "Line could not be parsed: $line\n";
      }
}