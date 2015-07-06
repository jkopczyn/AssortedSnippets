dict = Hash.new() {|hash, key| hash[key] = Hash.new() {|hash, key| hash[key] = {} }
 }
temp = ""
File.open("GroovesharkBackup.txt",'r').readlines.each do |line|
  if line.strip[-1] != '"'
    temp += line.strip
  else
    line = "#{temp} #{line}"
    song, artist, album = line.split('","')
    song = (song.strip or "").sub(/^"|"$/, '')
    artist = (artist.strip or "").sub(/^"|"$/, '')
    album = (album.strip or "").sub(/^"|"$/, '')
    dict[artist][album][song] = true 
    temp = ""
  end
end
File.open("GroovesharkBackup.xspf",'w') do |file|
  file.puts '<?xml version="1.0" encoding="UTF-8"?>
  <playlist version="1" xmlns="http://xspf.org/ns/0/">
    <trackList>'
  dict.keys.each do |artist|
    next if artist == "ArtistName"
    dict[artist].keys.each do |album|
      dict[artist][album].keys.each do |song|
        file.puts <<-XML
      <track>
        <title>#{song}</title>
        <album>#{album}</album>
        <creator>#{artist}</creator>
      </track>
        XML
      end
    end
  end
  file.puts '</trackList>
  </playlist>'
end
