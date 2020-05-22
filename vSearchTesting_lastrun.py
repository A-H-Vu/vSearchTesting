#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 22, 2020, at 16:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'vSearchTesting'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\v-search-testing\\vSearchTesting_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this experiment blah blah\nSpace to continue',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trialFix1 = visual.TextStim(win=win, name='trialFix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
l11 = visual.ImageStim(
    win=win,
    name='l11', 
    image='L11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
l12 = visual.ImageStim(
    win=win,
    name='l12', 
    image='L12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l21 = visual.ImageStim(
    win=win,
    name='l21', 
    image='L21.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
l22 = visual.ImageStim(
    win=win,
    name='l22', 
    image='L22.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
t11 = visual.ImageStim(
    win=win,
    name='t11', 
    image='T11.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
t12 = visual.ImageStim(
    win=win,
    name='t12', 
    image='T12.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
tT = visual.ImageStim(
    win=win,
    name='tT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trialResp1 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Thanks',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instruction1Components = [instr1, keyResp1]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [text]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation1"-------
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchTesting1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    l11.setPos([loc1,loc2])
    l12.setPos([loc3,loc4])
    l21.setPos([loc5,loc6])
    l22.setPos([loc7,loc8])
    t11.setPos([loc9,loc10])
    t12.setPos([loc11,12])
    tT.setPos([loc13,loc14])
    trialResp1.keys = []
    trialResp1.rt = []
    _trialResp1_allKeys = []
    # keep track of which components have finished
    trial1Components = [trialFix1, l11, l12, l21, l22, t11, t12, tT, trialResp1]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialFix1* updates
        if trialFix1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix1.frameNStart = frameN  # exact frame index
            trialFix1.tStart = t  # local t and not account for scr refresh
            trialFix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix1, 'tStartRefresh')  # time at next scr refresh
            trialFix1.setAutoDraw(True)
        if trialFix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix1.tStop = t  # not accounting for scr refresh
                trialFix1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix1, 'tStopRefresh')  # time at next scr refresh
                trialFix1.setAutoDraw(False)
        
        # *l11* updates
        if l11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l11.frameNStart = frameN  # exact frame index
            l11.tStart = t  # local t and not account for scr refresh
            l11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l11, 'tStartRefresh')  # time at next scr refresh
            l11.setAutoDraw(True)
        if l11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                l11.tStop = t  # not accounting for scr refresh
                l11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l11, 'tStopRefresh')  # time at next scr refresh
                l11.setAutoDraw(False)
        
        # *l12* updates
        if l12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l12.frameNStart = frameN  # exact frame index
            l12.tStart = t  # local t and not account for scr refresh
            l12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l12, 'tStartRefresh')  # time at next scr refresh
            l12.setAutoDraw(True)
        if l12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                l12.tStop = t  # not accounting for scr refresh
                l12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l12, 'tStopRefresh')  # time at next scr refresh
                l12.setAutoDraw(False)
        
        # *l21* updates
        if l21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l21.frameNStart = frameN  # exact frame index
            l21.tStart = t  # local t and not account for scr refresh
            l21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l21, 'tStartRefresh')  # time at next scr refresh
            l21.setAutoDraw(True)
        if l21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l21.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                l21.tStop = t  # not accounting for scr refresh
                l21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l21, 'tStopRefresh')  # time at next scr refresh
                l21.setAutoDraw(False)
        
        # *l22* updates
        if l22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l22.frameNStart = frameN  # exact frame index
            l22.tStart = t  # local t and not account for scr refresh
            l22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l22, 'tStartRefresh')  # time at next scr refresh
            l22.setAutoDraw(True)
        if l22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l22.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                l22.tStop = t  # not accounting for scr refresh
                l22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l22, 'tStopRefresh')  # time at next scr refresh
                l22.setAutoDraw(False)
        
        # *t11* updates
        if t11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t11.frameNStart = frameN  # exact frame index
            t11.tStart = t  # local t and not account for scr refresh
            t11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t11, 'tStartRefresh')  # time at next scr refresh
            t11.setAutoDraw(True)
        if t11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > t11.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                t11.tStop = t  # not accounting for scr refresh
                t11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(t11, 'tStopRefresh')  # time at next scr refresh
                t11.setAutoDraw(False)
        
        # *t12* updates
        if t12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t12.frameNStart = frameN  # exact frame index
            t12.tStart = t  # local t and not account for scr refresh
            t12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t12, 'tStartRefresh')  # time at next scr refresh
            t12.setAutoDraw(True)
        if t12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > t12.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                t12.tStop = t  # not accounting for scr refresh
                t12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(t12, 'tStopRefresh')  # time at next scr refresh
                t12.setAutoDraw(False)
        
        # *tT* updates
        if tT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tT.frameNStart = frameN  # exact frame index
            tT.tStart = t  # local t and not account for scr refresh
            tT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tT, 'tStartRefresh')  # time at next scr refresh
            tT.setAutoDraw(True)
        if tT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tT.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                tT.tStop = t  # not accounting for scr refresh
                tT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tT, 'tStopRefresh')  # time at next scr refresh
                tT.setAutoDraw(False)
        
        # *trialResp1* updates
        waitOnFlip = False
        if trialResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp1.frameNStart = frameN  # exact frame index
            trialResp1.tStart = t  # local t and not account for scr refresh
            trialResp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp1, 'tStartRefresh')  # time at next scr refresh
            trialResp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialResp1.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                trialResp1.tStop = t  # not accounting for scr refresh
                trialResp1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialResp1, 'tStopRefresh')  # time at next scr refresh
                trialResp1.status = FINISHED
        if trialResp1.status == STARTED and not waitOnFlip:
            theseKeys = trialResp1.getKeys(keyList=['space'], waitRelease=False)
            _trialResp1_allKeys.extend(theseKeys)
            if len(_trialResp1_allKeys):
                trialResp1.keys = _trialResp1_allKeys[-1].name  # just the last key pressed
                trialResp1.rt = _trialResp1_allKeys[-1].rt
                # was this correct?
                if (trialResp1.keys == str(corrAns)) or (trialResp1.keys == corrAns):
                    trialResp1.corr = 1
                else:
                    trialResp1.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials1.addData('trialFix1.started', trialFix1.tStartRefresh)
    trials1.addData('trialFix1.stopped', trialFix1.tStopRefresh)
    trials1.addData('l11.started', l11.tStartRefresh)
    trials1.addData('l11.stopped', l11.tStopRefresh)
    trials1.addData('l12.started', l12.tStartRefresh)
    trials1.addData('l12.stopped', l12.tStopRefresh)
    trials1.addData('l21.started', l21.tStartRefresh)
    trials1.addData('l21.stopped', l21.tStopRefresh)
    trials1.addData('l22.started', l22.tStartRefresh)
    trials1.addData('l22.stopped', l22.tStopRefresh)
    trials1.addData('t11.started', t11.tStartRefresh)
    trials1.addData('t11.stopped', t11.tStopRefresh)
    trials1.addData('t12.started', t12.tStartRefresh)
    trials1.addData('t12.stopped', t12.tStopRefresh)
    trials1.addData('tT.started', tT.tStartRefresh)
    trials1.addData('tT.stopped', tT.tStopRefresh)
    # check responses
    if trialResp1.keys in ['', [], None]:  # No response was made
        trialResp1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp1.corr = 1;  # correct non-response
        else:
           trialResp1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trialResp1.keys',trialResp1.keys)
    trials1.addData('trialResp1.corr', trialResp1.corr)
    if trialResp1.keys != None:  # we had a response
        trials1.addData('trialResp1.rt', trialResp1.rt)
    trials1.addData('trialResp1.started', trialResp1.tStartRefresh)
    trials1.addData('trialResp1.stopped', trialResp1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
