def detour(a,b,c,d)
  #these are the total lengths, but a<->c and b<->d are in both
  #path1 = distance(a,c)+distance(c,d)+distance(d,b)
  #path2 = distance(c,a)+distance(a,b)+distance(b,d)
  #so the shorter detour distance is the shorter route distance
  #assuming it's symmetric, which is a smaller simplification than pythagorean
  #distance
  [distance(a,b), distance(c,d)].min
end

def distance(a,b)
  ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(0.5)
end
