source_filename = "test"
target datalayout = "e-m:e-p:64:64-i64:64-f80:128-n8:16:32:64-S128"

@global_var_4028 = global i64 0
@global_var_3fe0 = local_unnamed_addr global i64 0
@global_var_2004 = constant [12 x i8] c"Output: %s\0A\00"
@global_var_2010 = constant [5 x i8] c"%02x\00"
@0 = external global i32

define i64 @_init() local_unnamed_addr {
dec_label_pc_1000:
  %rax.0.reg2mem = alloca i64, !insn.addr !0
  %0 = load i64, i64* inttoptr (i64 16336 to i64*), align 16, !insn.addr !1
  %1 = icmp eq i64 %0, 0, !insn.addr !2
  store i64 0, i64* %rax.0.reg2mem, !insn.addr !3
  br i1 %1, label %dec_label_pc_1012, label %dec_label_pc_1010, !insn.addr !3

dec_label_pc_1010:                                ; preds = %dec_label_pc_1000
  call void @__gmon_start__(), !insn.addr !4
  store i64 ptrtoint (i32* @0 to i64), i64* %rax.0.reg2mem, !insn.addr !4
  br label %dec_label_pc_1012, !insn.addr !4

dec_label_pc_1012:                                ; preds = %dec_label_pc_1010, %dec_label_pc_1000
  %rax.0.reload = load i64, i64* %rax.0.reg2mem
  ret i64 %rax.0.reload, !insn.addr !5
}

define i32 @function_1030(i32 %c) local_unnamed_addr {
dec_label_pc_1030:
  %0 = call i32 @putchar(i32 %c), !insn.addr !6
  ret i32 %0, !insn.addr !6
}

define i32 @function_1040(i8* %s) local_unnamed_addr {
dec_label_pc_1040:
  %0 = call i32 @strlen(i8* %s), !insn.addr !7
  ret i32 %0, !insn.addr !7
}

define i32 @function_1050(i8* %format, ...) local_unnamed_addr {
dec_label_pc_1050:
  %0 = call i32 (i8*, ...) @printf(i8* %format), !insn.addr !8
  ret i32 %0, !insn.addr !8
}

define void @function_1060(i64* %d) local_unnamed_addr {
dec_label_pc_1060:
  call void @__cxa_finalize(i64* %d), !insn.addr !9
  ret void, !insn.addr !9
}

define i64 @_start(i64 %arg1, i64 %arg2, i64 %arg3, i64 %arg4, i64 %arg5, i64 %arg6) local_unnamed_addr {
dec_label_pc_1070:
  %stack_var_8 = alloca i64, align 8
  %0 = trunc i64 %arg6 to i32, !insn.addr !10
  %1 = bitcast i64* %stack_var_8 to i8**, !insn.addr !10
  %2 = inttoptr i64 %arg3 to void ()*, !insn.addr !10
  %3 = call i32 @__libc_start_main(i64 4441, i32 %0, i8** nonnull %1, void ()* null, void ()* null, void ()* %2), !insn.addr !10
  %4 = call i64 @__asm_hlt(), !insn.addr !11
  unreachable, !insn.addr !11
}

define i64 @deregister_tm_clones() local_unnamed_addr {
dec_label_pc_10a0:
  ret i64 ptrtoint (i64* @global_var_4028 to i64), !insn.addr !12
}

define i64 @register_tm_clones() local_unnamed_addr {
dec_label_pc_10d0:
  ret i64 0, !insn.addr !13
}

define i64 @__do_global_dtors_aux() local_unnamed_addr {
dec_label_pc_1110:
  %0 = alloca i64
  %1 = load i64, i64* %0
  %2 = load i8, i8* bitcast (i64* @global_var_4028 to i8*), align 8, !insn.addr !14
  %3 = icmp eq i8 %2, 0, !insn.addr !14
  %4 = icmp eq i1 %3, false, !insn.addr !15
  br i1 %4, label %dec_label_pc_1148, label %dec_label_pc_111d, !insn.addr !15

dec_label_pc_111d:                                ; preds = %dec_label_pc_1110
  %5 = load i64, i64* @global_var_3fe0, align 8, !insn.addr !16
  %6 = icmp eq i64 %5, 0, !insn.addr !16
  br i1 %6, label %dec_label_pc_1137, label %dec_label_pc_112b, !insn.addr !17

dec_label_pc_112b:                                ; preds = %dec_label_pc_111d
  %7 = load i64, i64* inttoptr (i64 16416 to i64*), align 32, !insn.addr !18
  %8 = inttoptr i64 %7 to i64*, !insn.addr !19
  call void @__cxa_finalize(i64* %8), !insn.addr !19
  br label %dec_label_pc_1137, !insn.addr !19

dec_label_pc_1137:                                ; preds = %dec_label_pc_112b, %dec_label_pc_111d
  %9 = call i64 @deregister_tm_clones(), !insn.addr !20
  store i8 1, i8* bitcast (i64* @global_var_4028 to i8*), align 8, !insn.addr !21
  ret i64 %9, !insn.addr !22

dec_label_pc_1148:                                ; preds = %dec_label_pc_1110
  ret i64 %1, !insn.addr !23
}

define i64 @frame_dummy() local_unnamed_addr {
dec_label_pc_1150:
  %0 = call i64 @register_tm_clones(), !insn.addr !24
  ret i64 %0, !insn.addr !24
}

define i64 @main(i64 %argc, i8** %argv) local_unnamed_addr {
dec_label_pc_1159:
  %stack_var_-40 = alloca i64, align 8
  store i64 7596519730561841475, i64* %stack_var_-40, align 8, !insn.addr !25
  %0 = call i64 @a(i64* nonnull %stack_var_-40), !insn.addr !26
  %1 = call i64 @b(i64* nonnull %stack_var_-40), !insn.addr !27
  %2 = call i64 @c(i64* nonnull %stack_var_-40, i64 90), !insn.addr !28
  %3 = call i64 @d(i64* nonnull %stack_var_-40, i64 3), !insn.addr !29
  %4 = call i64 @e(i64* nonnull %stack_var_-40), !insn.addr !30
  %5 = call i64 @f(i64* nonnull %stack_var_-40), !insn.addr !31
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @global_var_2004, i64 0, i64 0), i64* nonnull %stack_var_-40), !insn.addr !32
  ret i64 0, !insn.addr !33
}

define i64 @a(i64* %arg1) local_unnamed_addr {
dec_label_pc_11ff:
  %.lcssa.reg2mem = alloca i64, !insn.addr !34
  %storemerge1.reg2mem = alloca i32, !insn.addr !34
  %0 = ptrtoint i64* %arg1 to i64
  %1 = bitcast i64* %arg1 to i8*, !insn.addr !35
  %2 = call i32 @strlen(i8* %1), !insn.addr !35
  %3 = icmp eq i32 %2, 0, !insn.addr !36
  store i32 0, i32* %storemerge1.reg2mem, !insn.addr !37
  store i64 0, i64* %.lcssa.reg2mem, !insn.addr !37
  br i1 %3, label %dec_label_pc_1254, label %dec_label_pc_1215, !insn.addr !37

dec_label_pc_1215:                                ; preds = %dec_label_pc_11ff, %dec_label_pc_1215
  %storemerge1.reload = load i32, i32* %storemerge1.reg2mem
  %4 = sext i32 %storemerge1.reload to i64, !insn.addr !38
  %5 = add i64 %4, %0, !insn.addr !39
  %6 = inttoptr i64 %5 to i8*, !insn.addr !40
  %7 = load i8, i8* %6, align 1, !insn.addr !40
  %8 = add i8 %7, 1, !insn.addr !41
  store i8 %8, i8* %6, align 1, !insn.addr !42
  %9 = add nuw i32 %storemerge1.reload, 1, !insn.addr !43
  %10 = call i32 @strlen(i8* %1), !insn.addr !35
  %11 = icmp ult i32 %9, %10, !insn.addr !36
  store i32 %9, i32* %storemerge1.reg2mem, !insn.addr !37
  br i1 %11, label %dec_label_pc_1215, label %dec_label_pc_123d.dec_label_pc_1254_crit_edge, !insn.addr !37

dec_label_pc_123d.dec_label_pc_1254_crit_edge:    ; preds = %dec_label_pc_1215
  %phitmp = sext i32 %10 to i64
  store i64 %phitmp, i64* %.lcssa.reg2mem
  br label %dec_label_pc_1254

dec_label_pc_1254:                                ; preds = %dec_label_pc_11ff, %dec_label_pc_123d.dec_label_pc_1254_crit_edge
  %.lcssa.reload = load i64, i64* %.lcssa.reg2mem
  ret i64 %.lcssa.reload, !insn.addr !44

; uselistorder directives
  uselistorder i8* %1, { 1, 0 }
  uselistorder i32* %storemerge1.reg2mem, { 2, 0, 1 }
  uselistorder i64* %.lcssa.reg2mem, { 0, 2, 1 }
  uselistorder label %dec_label_pc_1254, { 1, 0 }
  uselistorder label %dec_label_pc_1215, { 1, 0 }
}

define i64 @b(i64* %arg1) local_unnamed_addr {
dec_label_pc_125c:
  %stack_var_-12.0.lcssa.reg2mem = alloca i64, !insn.addr !45
  %indvars.iv.reg2mem = alloca i64, !insn.addr !45
  %0 = bitcast i64* %arg1 to i8*, !insn.addr !46
  %1 = call i32 @strlen(i8* %0), !insn.addr !46
  %2 = add i32 %1, -1, !insn.addr !47
  %3 = icmp sgt i32 %2, 0, !insn.addr !48
  store i64 0, i64* %stack_var_-12.0.lcssa.reg2mem, !insn.addr !48
  br i1 %3, label %dec_label_pc_1283.preheader, label %dec_label_pc_12dc, !insn.addr !48

dec_label_pc_1283.preheader:                      ; preds = %dec_label_pc_125c
  %4 = ptrtoint i64* %arg1 to i64
  %wide.trip.count = zext i32 %2 to i64
  store i64 0, i64* %indvars.iv.reg2mem
  br label %dec_label_pc_1283

dec_label_pc_1283:                                ; preds = %dec_label_pc_1283.preheader, %dec_label_pc_1283
  %indvars.iv.reload = load i64, i64* %indvars.iv.reg2mem
  %5 = add i64 %indvars.iv.reload, %4, !insn.addr !49
  %6 = inttoptr i64 %5 to i8*, !insn.addr !50
  %7 = load i8, i8* %6, align 1, !insn.addr !50
  %8 = sext i8 %7 to i64, !insn.addr !51
  %9 = add i64 %8, %4, !insn.addr !52
  %10 = inttoptr i64 %9 to i8*, !insn.addr !53
  %11 = load i8, i8* %10, align 1, !insn.addr !53
  store i8 %11, i8* %6, align 1, !insn.addr !54
  store i8 %7, i8* %10, align 1, !insn.addr !55
  %indvars.iv.next = add nuw nsw i64 %indvars.iv.reload, 1
  %exitcond = icmp eq i64 %indvars.iv.next, %wide.trip.count
  store i64 %indvars.iv.next, i64* %indvars.iv.reg2mem, !insn.addr !48
  store i64 %wide.trip.count, i64* %stack_var_-12.0.lcssa.reg2mem, !insn.addr !48
  br i1 %exitcond, label %dec_label_pc_12dc, label %dec_label_pc_1283, !insn.addr !48

dec_label_pc_12dc:                                ; preds = %dec_label_pc_1283, %dec_label_pc_125c
  %stack_var_-12.0.lcssa.reload = load i64, i64* %stack_var_-12.0.lcssa.reg2mem
  ret i64 %stack_var_-12.0.lcssa.reload, !insn.addr !56

; uselistorder directives
  uselistorder i64* %indvars.iv.reg2mem, { 2, 0, 1 }
  uselistorder i64* %arg1, { 1, 0 }
  uselistorder label %dec_label_pc_1283, { 1, 0 }
}

define i64 @c(i64* %arg1, i64 %arg2) local_unnamed_addr {
dec_label_pc_12e0:
  %.lcssa.reg2mem = alloca i64, !insn.addr !57
  %storemerge2.reg2mem = alloca i32, !insn.addr !57
  %0 = bitcast i64* %arg1 to i8*, !insn.addr !58
  %1 = call i32 @strlen(i8* %0), !insn.addr !58
  %2 = icmp eq i32 %1, 0, !insn.addr !59
  store i64 0, i64* %.lcssa.reg2mem, !insn.addr !60
  br i1 %2, label %dec_label_pc_1338, label %dec_label_pc_12fb.lr.ph, !insn.addr !60

dec_label_pc_12fb.lr.ph:                          ; preds = %dec_label_pc_12e0
  %3 = ptrtoint i64* %arg1 to i64
  %4 = trunc i64 %arg2 to i8, !insn.addr !61
  store i32 0, i32* %storemerge2.reg2mem
  br label %dec_label_pc_12fb

dec_label_pc_12fb:                                ; preds = %dec_label_pc_12fb.lr.ph, %dec_label_pc_12fb
  %storemerge2.reload = load i32, i32* %storemerge2.reg2mem
  %5 = sext i32 %storemerge2.reload to i64, !insn.addr !62
  %6 = add i64 %5, %3, !insn.addr !63
  %7 = inttoptr i64 %6 to i8*, !insn.addr !64
  %8 = load i8, i8* %7, align 1, !insn.addr !64
  %9 = xor i8 %8, %4, !insn.addr !61
  store i8 %9, i8* %7, align 1, !insn.addr !65
  %10 = add nuw i32 %storemerge2.reload, 1, !insn.addr !66
  %11 = call i32 @strlen(i8* %0), !insn.addr !58
  %12 = icmp ult i32 %10, %11, !insn.addr !59
  store i32 %10, i32* %storemerge2.reg2mem, !insn.addr !60
  br i1 %12, label %dec_label_pc_12fb, label %dec_label_pc_1321.dec_label_pc_1338_crit_edge, !insn.addr !60

dec_label_pc_1321.dec_label_pc_1338_crit_edge:    ; preds = %dec_label_pc_12fb
  %phitmp = sext i32 %11 to i64
  store i64 %phitmp, i64* %.lcssa.reg2mem
  br label %dec_label_pc_1338

dec_label_pc_1338:                                ; preds = %dec_label_pc_12e0, %dec_label_pc_1321.dec_label_pc_1338_crit_edge
  %.lcssa.reload = load i64, i64* %.lcssa.reg2mem
  ret i64 %.lcssa.reload, !insn.addr !67

; uselistorder directives
  uselistorder i8* %0, { 1, 0 }
  uselistorder i32* %storemerge2.reg2mem, { 1, 0, 2 }
  uselistorder i64* %.lcssa.reg2mem, { 0, 2, 1 }
  uselistorder i64* %arg1, { 1, 0 }
  uselistorder label %dec_label_pc_1338, { 1, 0 }
  uselistorder label %dec_label_pc_12fb, { 1, 0 }
}

define i64 @d(i64* %arg1, i64 %arg2) local_unnamed_addr {
dec_label_pc_1340:
  %.lcssa.reg2mem = alloca i64, !insn.addr !68
  %storemerge3.reg2mem = alloca i32, !insn.addr !68
  %0 = bitcast i64* %arg1 to i8*, !insn.addr !69
  %1 = call i32 @strlen(i8* %0), !insn.addr !69
  %2 = icmp eq i32 %1, 0, !insn.addr !70
  store i64 0, i64* %.lcssa.reg2mem, !insn.addr !71
  br i1 %2, label %dec_label_pc_13bd, label %dec_label_pc_1359.lr.ph, !insn.addr !71

dec_label_pc_1359.lr.ph:                          ; preds = %dec_label_pc_1340
  %3 = ptrtoint i64* %arg1 to i64
  %4 = trunc i64 %arg2 to i32, !insn.addr !72
  %5 = urem i32 %4, 32, !insn.addr !72
  %6 = icmp eq i32 %5, 0, !insn.addr !72
  %7 = sub i32 8, %4, !insn.addr !73
  %8 = urem i32 %7, 32, !insn.addr !74
  %9 = icmp eq i32 %8, 0, !insn.addr !74
  store i32 0, i32* %storemerge3.reg2mem
  br label %dec_label_pc_1359

dec_label_pc_1359:                                ; preds = %dec_label_pc_1359.lr.ph, %dec_label_pc_1359
  %storemerge3.reload = load i32, i32* %storemerge3.reg2mem
  %10 = sext i32 %storemerge3.reload to i64, !insn.addr !75
  %11 = add i64 %10, %3, !insn.addr !76
  %12 = inttoptr i64 %11 to i8*, !insn.addr !77
  %13 = load i8, i8* %12, align 1, !insn.addr !77
  %14 = zext i8 %13 to i32
  %15 = shl i32 %14, %5
  %16 = trunc i32 %15 to i8
  %rdx.0 = select i1 %6, i8 %13, i8 %16
  %17 = lshr i32 %14, %8
  %18 = trunc i32 %17 to i8
  %rdx.1 = select i1 %9, i8 %13, i8 %18
  %19 = or i8 %rdx.0, %rdx.1
  store i8 %19, i8* %12, align 1, !insn.addr !78
  %20 = add nuw i32 %storemerge3.reload, 1, !insn.addr !79
  %21 = call i32 @strlen(i8* %0), !insn.addr !69
  %22 = icmp ult i32 %20, %21, !insn.addr !70
  store i32 %20, i32* %storemerge3.reg2mem, !insn.addr !71
  br i1 %22, label %dec_label_pc_1359, label %dec_label_pc_13a6.dec_label_pc_13bd_crit_edge, !insn.addr !71

dec_label_pc_13a6.dec_label_pc_13bd_crit_edge:    ; preds = %dec_label_pc_1359
  %phitmp = sext i32 %21 to i64
  store i64 %phitmp, i64* %.lcssa.reg2mem
  br label %dec_label_pc_13bd

dec_label_pc_13bd:                                ; preds = %dec_label_pc_1340, %dec_label_pc_13a6.dec_label_pc_13bd_crit_edge
  %.lcssa.reload = load i64, i64* %.lcssa.reg2mem
  ret i64 %.lcssa.reload, !insn.addr !80

; uselistorder directives
  uselistorder i32 %14, { 1, 0 }
  uselistorder i32 %8, { 1, 0 }
  uselistorder i32 %5, { 1, 0 }
  uselistorder i32 %4, { 1, 0 }
  uselistorder i8* %0, { 1, 0 }
  uselistorder i32* %storemerge3.reg2mem, { 1, 0, 2 }
  uselistorder i64* %.lcssa.reg2mem, { 0, 2, 1 }
  uselistorder i64* %arg1, { 1, 0 }
  uselistorder label %dec_label_pc_13bd, { 1, 0 }
  uselistorder label %dec_label_pc_1359, { 1, 0 }
}

define i64 @e(i64* %arg1) local_unnamed_addr {
dec_label_pc_13c5:
  %.lcssa.reg2mem = alloca i64, !insn.addr !81
  %storemerge1.reg2mem = alloca i32, !insn.addr !81
  %.reg2mem = alloca i64, !insn.addr !81
  %0 = ptrtoint i64* %arg1 to i64
  %1 = bitcast i64* %arg1 to i8*, !insn.addr !82
  %2 = call i32 @strlen(i8* %1), !insn.addr !82
  %3 = icmp eq i32 %2, 1, !insn.addr !83
  store i64 0, i64* %.reg2mem, !insn.addr !84
  store i32 0, i32* %storemerge1.reg2mem, !insn.addr !84
  store i64 0, i64* %.lcssa.reg2mem, !insn.addr !84
  br i1 %3, label %dec_label_pc_1445, label %dec_label_pc_13db, !insn.addr !84

dec_label_pc_13db:                                ; preds = %dec_label_pc_13c5, %dec_label_pc_13db
  %storemerge1.reload = load i32, i32* %storemerge1.reg2mem
  %.reload = load i64, i64* %.reg2mem
  %4 = add i64 %.reload, %0, !insn.addr !85
  %5 = inttoptr i64 %4 to i8*, !insn.addr !86
  %6 = load i8, i8* %5, align 1, !insn.addr !86
  %7 = or i64 %.reload, 1, !insn.addr !87
  %8 = add i64 %7, %0, !insn.addr !88
  %9 = inttoptr i64 %8 to i8*, !insn.addr !89
  %10 = load i8, i8* %9, align 1, !insn.addr !89
  store i8 %10, i8* %5, align 1, !insn.addr !90
  %11 = or i32 %storemerge1.reload, 1
  %12 = sext i32 %11 to i64, !insn.addr !91
  %13 = add i64 %12, %0, !insn.addr !92
  %14 = inttoptr i64 %13 to i8*, !insn.addr !93
  store i8 %6, i8* %14, align 1, !insn.addr !93
  %15 = add i32 %storemerge1.reload, 2, !insn.addr !94
  %16 = sext i32 %15 to i64, !insn.addr !95
  %17 = call i32 @strlen(i8* %1), !insn.addr !82
  %18 = sext i32 %17 to i64, !insn.addr !82
  %19 = add nsw i64 %18, -1, !insn.addr !96
  %20 = icmp ugt i64 %19, %16, !insn.addr !83
  store i64 %16, i64* %.reg2mem, !insn.addr !84
  store i32 %15, i32* %storemerge1.reg2mem, !insn.addr !84
  store i64 %19, i64* %.lcssa.reg2mem, !insn.addr !84
  br i1 %20, label %dec_label_pc_13db, label %dec_label_pc_1445, !insn.addr !84

dec_label_pc_1445:                                ; preds = %dec_label_pc_13db, %dec_label_pc_13c5
  %.lcssa.reload = load i64, i64* %.lcssa.reg2mem
  ret i64 %.lcssa.reload, !insn.addr !97

; uselistorder directives
  uselistorder i32 %storemerge1.reload, { 1, 0 }
  uselistorder i8* %1, { 1, 0 }
  uselistorder i64* %.reg2mem, { 2, 0, 1 }
  uselistorder i32* %storemerge1.reg2mem, { 2, 0, 1 }
  uselistorder label %dec_label_pc_13db, { 1, 0 }
}

define i64 @f(i64* %arg1) local_unnamed_addr {
dec_label_pc_144d:
  %indvars.iv.reg2mem = alloca i64, !insn.addr !98
  %0 = bitcast i64* %arg1 to i8*, !insn.addr !99
  %1 = call i32 @strlen(i8* %0), !insn.addr !99
  %2 = icmp sgt i32 %1, 0, !insn.addr !100
  br i1 %2, label %dec_label_pc_1471.preheader, label %dec_label_pc_14a6, !insn.addr !100

dec_label_pc_1471.preheader:                      ; preds = %dec_label_pc_144d
  %3 = ptrtoint i64* %arg1 to i64
  %wide.trip.count = zext i32 %1 to i64
  store i64 0, i64* %indvars.iv.reg2mem
  br label %dec_label_pc_1471

dec_label_pc_1471:                                ; preds = %dec_label_pc_1471.preheader, %dec_label_pc_1471
  %indvars.iv.reload = load i64, i64* %indvars.iv.reg2mem
  %4 = add i64 %indvars.iv.reload, %3, !insn.addr !101
  %5 = inttoptr i64 %4 to i8*, !insn.addr !102
  %6 = load i8, i8* %5, align 1, !insn.addr !102
  %7 = sext i8 %6 to i32, !insn.addr !103
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @global_var_2010, i64 0, i64 0), i32 %7), !insn.addr !104
  %indvars.iv.next = add nuw nsw i64 %indvars.iv.reload, 1
  %exitcond = icmp eq i64 %indvars.iv.next, %wide.trip.count
  store i64 %indvars.iv.next, i64* %indvars.iv.reg2mem, !insn.addr !100
  br i1 %exitcond, label %dec_label_pc_14a6, label %dec_label_pc_1471, !insn.addr !100

dec_label_pc_14a6:                                ; preds = %dec_label_pc_1471, %dec_label_pc_144d
  %9 = call i32 @putchar(i32 10), !insn.addr !105
  %10 = sext i32 %9 to i64, !insn.addr !105
  ret i64 %10, !insn.addr !106

; uselistorder directives
  uselistorder i64* %indvars.iv.reg2mem, { 2, 0, 1 }
  uselistorder i64 1, { 0, 2, 1 }
  uselistorder i64 0, { 11, 12, 0, 1, 2, 3, 4, 6, 5, 7, 9, 13, 14, 17, 10, 8, 18, 15, 16 }
  uselistorder i32 0, { 4, 0, 1, 9, 10, 5, 2, 6, 7, 3, 8 }
  uselistorder i32 (i8*)* @strlen, { 9, 8, 0, 7, 1, 6, 2, 5, 4, 3, 10 }
  uselistorder i64* %arg1, { 1, 0 }
  uselistorder label %dec_label_pc_1471, { 1, 0 }
}

define i64 @_fini() local_unnamed_addr {
dec_label_pc_14b4:
  %0 = alloca i64
  %1 = load i64, i64* %0
  ret i64 %1, !insn.addr !107

; uselistorder directives
  uselistorder i32 1, { 1, 2, 16, 15, 5, 4, 3, 19, 7, 6, 20, 9, 8, 11, 10, 21, 13, 12, 17, 0, 18, 14 }
}

declare i32 @__libc_start_main(i64, i32, i8**, void ()*, void ()*, void ()*) local_unnamed_addr

declare void @__gmon_start__() local_unnamed_addr

declare void @__cxa_finalize(i64*) local_unnamed_addr

declare i32 @putchar(i32) local_unnamed_addr

declare i32 @strlen(i8*) local_unnamed_addr

declare i32 @printf(i8*, ...) local_unnamed_addr

declare i64 @__asm_hlt() local_unnamed_addr

!0 = !{i64 4096}
!1 = !{i64 4100}
!2 = !{i64 4107}
!3 = !{i64 4110}
!4 = !{i64 4112}
!5 = !{i64 4118}
!6 = !{i64 4144}
!7 = !{i64 4160}
!8 = !{i64 4176}
!9 = !{i64 4192}
!10 = !{i64 4235}
!11 = !{i64 4241}
!12 = !{i64 4296}
!13 = !{i64 4360}
!14 = !{i64 4372}
!15 = !{i64 4379}
!16 = !{i64 4382}
!17 = !{i64 4393}
!18 = !{i64 4395}
!19 = !{i64 4402}
!20 = !{i64 4407}
!21 = !{i64 4412}
!22 = !{i64 4420}
!23 = !{i64 4424}
!24 = !{i64 4436}
!25 = !{i64 4469}
!26 = !{i64 4498}
!27 = !{i64 4510}
!28 = !{i64 4527}
!29 = !{i64 4544}
!30 = !{i64 4556}
!31 = !{i64 4568}
!32 = !{i64 4595}
!33 = !{i64 4606}
!34 = !{i64 4607}
!35 = !{i64 4682}
!36 = !{i64 4687}
!37 = !{i64 4690}
!38 = !{i64 4632}
!39 = !{i64 4639}
!40 = !{i64 4642}
!41 = !{i64 4645}
!42 = !{i64 4663}
!43 = !{i64 4665}
!44 = !{i64 4699}
!45 = !{i64 4700}
!46 = !{i64 4726}
!47 = !{i64 4731}
!48 = !{i64 4826}
!49 = !{i64 4749}
!50 = !{i64 4752}
!51 = !{i64 4758}
!52 = !{i64 4767}
!53 = !{i64 4783}
!54 = !{i64 4786}
!55 = !{i64 4804}
!56 = !{i64 4831}
!57 = !{i64 4832}
!58 = !{i64 4910}
!59 = !{i64 4915}
!60 = !{i64 4918}
!61 = !{i64 4888}
!62 = !{i64 4862}
!63 = !{i64 4869}
!64 = !{i64 4872}
!65 = !{i64 4891}
!66 = !{i64 4893}
!67 = !{i64 4927}
!68 = !{i64 4928}
!69 = !{i64 5043}
!70 = !{i64 5048}
!71 = !{i64 5051}
!72 = !{i64 4981}
!73 = !{i64 4996}
!74 = !{i64 5001}
!75 = !{i64 4956}
!76 = !{i64 4963}
!77 = !{i64 4966}
!78 = !{i64 5024}
!79 = !{i64 5026}
!80 = !{i64 5060}
!81 = !{i64 5061}
!82 = !{i64 5175}
!83 = !{i64 5184}
!84 = !{i64 5187}
!85 = !{i64 5093}
!86 = !{i64 5096}
!87 = !{i64 5107}
!88 = !{i64 5115}
!89 = !{i64 5131}
!90 = !{i64 5134}
!91 = !{i64 5141}
!92 = !{i64 5149}
!93 = !{i64 5156}
!94 = !{i64 5158}
!95 = !{i64 5165}
!96 = !{i64 5180}
!97 = !{i64 5196}
!98 = !{i64 5197}
!99 = !{i64 5216}
!100 = !{i64 5284}
!101 = !{i64 5243}
!102 = !{i64 5246}
!103 = !{i64 5252}
!104 = !{i64 5269}
!105 = !{i64 5291}
!106 = !{i64 5298}
!107 = !{i64 5308}
