vim9script
# set rtp^=/tmp/vim-perf
# vimperf#setup()
def Estimate(t: string)
  # vimperf#start('prof_' .. t .. '.out')
  var repeat = 3
  var n = 1000 / str2nr(t)
  var start = reltime()
  for _ in range(repeat)
    for __ in range(n)
      execute 'sleep' t
    endfor
  endfor
  var elapsed = reltimefloat(reltime(start)) / repeat
  # vimperf#stop()
  var calibrator = (n * str2nr(t) * (t =~# 'm$' ? 1 : 1000)) / (elapsed * 1000)
  echo printf('%dx sleep %s', n, t)
  echo printf('  Elapsed     = %f', elapsed)
  echo printf('  Unit        = %f', elapsed / n)
  echo printf('  Calibration = %f', calibrator)
  echo ''
enddef
sleep 1
Estimate('1m')
Estimate('10m')
Estimate('50m')
Estimate('100m')
Estimate('1000m')
