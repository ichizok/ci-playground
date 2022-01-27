" set rtp^=/tmp/vim-perf
" vimperf#setup()
func Estimate(t)
  " vimperf#start('prof_' .. a:t .. '.out')
  let repeat = 3
  let n = 1000 / str2nr(a:t)
  let start = reltime()
  for _ in range(repeat)
    for _ in range(n)
      execute 'sleep' a:t
    endfor
  endfor
  let elapsed = reltimefloat(reltime(start)) / repeat
  " vimperf#stop()
  let calibrator = (n * str2nr(a:t) * (a:t =~# 'm$' ? 1 : 1000)) / (elapsed * 1000)
  echo printf('%dx sleep %s', n, a:t)
  echo printf('  Elapsed     = %f', elapsed)
  echo printf('  Unit        = %f', elapsed / n)
  echo printf('  Calibration = %f', calibrator)
  echo ''
endfunc
sleep 1
call Estimate('1m')
call Estimate('10m')
call Estimate('50m')
call Estimate('100m')
call Estimate('1000m')
