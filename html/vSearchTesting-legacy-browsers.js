/*********************** 
 * Vsearchtesting Test *
 ***********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'vSearchTesting';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instruction1RoutineBegin());
flowScheduler.add(instruction1RoutineEachFrame());
flowScheduler.add(instruction1RoutineEnd());
flowScheduler.add(fixation1RoutineBegin());
flowScheduler.add(fixation1RoutineEachFrame());
flowScheduler.add(fixation1RoutineEnd());
const trials1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials1LoopBegin, trials1LoopScheduler);
flowScheduler.add(trials1LoopScheduler);
flowScheduler.add(trials1LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instruction1Clock;
var instr1;
var keyResp1;
var fixation1Clock;
var text;
var trial1Clock;
var trialFix1;
var l11;
var l12;
var l21;
var l22;
var t11;
var t12;
var tT;
var trialResp1;
var endClock;
var thanks;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction1"
  instruction1Clock = new util.Clock();
  instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr1',
    text: 'In this experiment blah blah\nSpace to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation1"
  fixation1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial1"
  trial1Clock = new util.Clock();
  trialFix1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialFix1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  l11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l11', units : undefined, 
    image : 'L11.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  l12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l12', units : undefined, 
    image : 'L12.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  l21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l21', units : undefined, 
    image : 'L21.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  l22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l22', units : undefined, 
    image : 'L22.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  t11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't11', units : undefined, 
    image : 'T11.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  t12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't12', units : undefined, 
    image : 'T12.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  tT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trialResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks',
    text: 'Thanks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _keyResp1_allKeys;
var instruction1Components;
function instruction1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction1'-------
    t = 0;
    instruction1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp1.keys = undefined;
    keyResp1.rt = undefined;
    _keyResp1_allKeys = [];
    // keep track of which components have finished
    instruction1Components = [];
    instruction1Components.push(instr1);
    instruction1Components.push(keyResp1);
    
    instruction1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instruction1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyResp1* updates
    if (t >= 0.0 && keyResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp1.tStart = t;  // (not accounting for frame time here)
      keyResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.clearEvents(); });
    }

    if (keyResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp1.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp1_allKeys = _keyResp1_allKeys.concat(theseKeys);
      if (_keyResp1_allKeys.length > 0) {
        keyResp1.keys = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].name;  // just the last key pressed
        keyResp1.rt = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instruction1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction1'-------
    instruction1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('keyResp1.keys', keyResp1.keys);
    if (typeof keyResp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp1.rt', keyResp1.rt);
        routineTimer.reset();
        }
    
    keyResp1.stop();
    // the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation1Components;
function fixation1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'fixation1'-------
    t = 0;
    fixation1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixation1Components = [];
    fixation1Components.push(text);
    
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function fixation1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'fixation1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixation1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'fixation1'-------
    fixation1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trials1;
var currentLoop;
function trials1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchTesting1.xlsx',
    seed: undefined, name: 'trials1'
  });
  psychoJS.experiment.addLoop(trials1); // add the loop to the experiment
  currentLoop = trials1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials1.forEach(function() {
    const snapshot = trials1.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trial1RoutineBegin(snapshot));
    thisScheduler.add(trial1RoutineEachFrame(snapshot));
    thisScheduler.add(trial1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials1LoopEnd() {
  psychoJS.experiment.removeLoop(trials1);

  return Scheduler.Event.NEXT;
}


var _trialResp1_allKeys;
var trial1Components;
function trial1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial1'-------
    t = 0;
    trial1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    l11.setPos([loc1, loc2]);
    l12.setPos([loc3, loc4]);
    l21.setPos([loc5, loc6]);
    l22.setPos([loc7, loc8]);
    t11.setPos([loc9, loc10]);
    t12.setPos([loc11, 12]);
    tT.setPos([loc13, loc14]);
    trialResp1.keys = undefined;
    trialResp1.rt = undefined;
    _trialResp1_allKeys = [];
    // keep track of which components have finished
    trial1Components = [];
    trial1Components.push(trialFix1);
    trial1Components.push(l11);
    trial1Components.push(l12);
    trial1Components.push(l21);
    trial1Components.push(l22);
    trial1Components.push(t11);
    trial1Components.push(t12);
    trial1Components.push(tT);
    trial1Components.push(trialResp1);
    
    trial1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trial1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trialFix1* updates
    if (t >= 3.0 && trialFix1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialFix1.tStart = t;  // (not accounting for frame time here)
      trialFix1.frameNStart = frameN;  // exact frame index
      
      trialFix1.setAutoDraw(true);
    }

    frameRemains = 3.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trialFix1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trialFix1.setAutoDraw(false);
    }
    
    // *l11* updates
    if (t >= 0.0 && l11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l11.tStart = t;  // (not accounting for frame time here)
      l11.frameNStart = frameN;  // exact frame index
      
      l11.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (l11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      l11.setAutoDraw(false);
    }
    
    // *l12* updates
    if (t >= 0.0 && l12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l12.tStart = t;  // (not accounting for frame time here)
      l12.frameNStart = frameN;  // exact frame index
      
      l12.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (l12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      l12.setAutoDraw(false);
    }
    
    // *l21* updates
    if (t >= 0.0 && l21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l21.tStart = t;  // (not accounting for frame time here)
      l21.frameNStart = frameN;  // exact frame index
      
      l21.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (l21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      l21.setAutoDraw(false);
    }
    
    // *l22* updates
    if (t >= 0.0 && l22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l22.tStart = t;  // (not accounting for frame time here)
      l22.frameNStart = frameN;  // exact frame index
      
      l22.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (l22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      l22.setAutoDraw(false);
    }
    
    // *t11* updates
    if (t >= 0.0 && t11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t11.tStart = t;  // (not accounting for frame time here)
      t11.frameNStart = frameN;  // exact frame index
      
      t11.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (t11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      t11.setAutoDraw(false);
    }
    
    // *t12* updates
    if (t >= 0.0 && t12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t12.tStart = t;  // (not accounting for frame time here)
      t12.frameNStart = frameN;  // exact frame index
      
      t12.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (t12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      t12.setAutoDraw(false);
    }
    
    // *tT* updates
    if (t >= 0.0 && tT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tT.tStart = t;  // (not accounting for frame time here)
      tT.frameNStart = frameN;  // exact frame index
      
      tT.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tT.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tT.setAutoDraw(false);
    }
    
    // *trialResp1* updates
    if (t >= 0.0 && trialResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialResp1.tStart = t;  // (not accounting for frame time here)
      trialResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trialResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trialResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trialResp1.clearEvents(); });
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trialResp1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trialResp1.status = PsychoJS.Status.FINISHED;
  }

    if (trialResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = trialResp1.getKeys({keyList: ['space'], waitRelease: false});
      _trialResp1_allKeys = _trialResp1_allKeys.concat(theseKeys);
      if (_trialResp1_allKeys.length > 0) {
        trialResp1.keys = _trialResp1_allKeys[_trialResp1_allKeys.length - 1].name;  // just the last key pressed
        trialResp1.rt = _trialResp1_allKeys[_trialResp1_allKeys.length - 1].rt;
        // was this correct?
        if (trialResp1.keys == corrAns) {
            trialResp1.corr = 1;
        } else {
            trialResp1.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial1'-------
    trial1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (trialResp1.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trialResp1.corr = 1;  // correct non-response
      } else {
         trialResp1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trialResp1.keys', trialResp1.keys);
    psychoJS.experiment.addData('trialResp1.corr', trialResp1.corr);
    if (typeof trialResp1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trialResp1.rt', trialResp1.rt);
        }
    
    trialResp1.stop();
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(thanks);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks* updates
    if (t >= 0.0 && thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks.tStart = t;  // (not accounting for frame time here)
      thanks.frameNStart = frameN;  // exact frame index
      
      thanks.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thanks.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
