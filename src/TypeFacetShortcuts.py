
import rfscripts
reload(rfscripts)
import rfscripts.RFMergePoints as RFMergePoints

from mojo.events import addObserver, removeObserver

class TypeFacetShortcuts:
#class TypeFacetShortcuts(EditingTool):
    def __init__(self):
        addObserver(self, "keyDown", "keyDown")

    def keyDown(self, eventMap):
        try:
            #print
            #print 'eventMap', eventMap
            event = eventMap['event']
            #print 'event.1', event
            #print dir(event)
            ##print type(event.keyCode)
            #print event.keyCode()
            #print type(event.keyCode())
            #print chr(event.keyCode())
            modifierFlags = event.modifierFlags()
            NSShiftKeyMask      = 1 << 17
            NSControlKeyMask    = 1 << 18
            NSAlternateKeyMask  = 1 << 19
            NSCommandKeyMask    = 1 << 20
            isCommand = (modifierFlags & NSCommandKeyMask) > 0
            #print 'modifierFlags', modifierFlags
            #print 'NSCommandKeyMask', NSCommandKeyMask
            #print 'isCommand', isCommand
            #print 'yo', chr(ord('4')), ord('4')
            #print 'characters', event.characters()
            #print 'charactersIgnoringModifiers', event.charactersIgnoringModifiers()
            
            characters = event.charactersIgnoringModifiers()
            if isCommand:
                if characters == '4': 
                    self.RFMergePointsNotUpdatingControlPoints()
                #elif characters == '4': 
                #    self.RFMergePointsNotUpdatingControlPoints()
        except Exception, e:
            print e.message
        #removeObserver(self, 'keyDown')
        ##print event.modifiers()
    
    def RFMergePointsNotUpdatingControlPoints(self):
        #import rfscripts
        #reload(rfscripts)
        #import rfscripts.RFMergePoints as RFMergePoints
        
        try:
            RFMergePoints.mergeSelectedPointsInCurrentGlyph(updateControlPoints=False)
        except Exception, e:
            from robofab.interface.all.dialogs import Message as Dialog
            Dialog(e.message, title='Error')
    
        
TypeFacetShortcuts()


#from mojo.events import EditingTool, installTool

#class TypeFacetShortcuts2(EditingTool):
#    #def __init__(self):
#    #    addObserver(self, "keyDown", "keyDown")

#    def keyDown(self, event):
#        print 'event', event
#        modifiers = self.getModifiers()
#        print 'modifiers', modifiers
#    #def myObserver(self, glyph, info):
#    #    print glyph, info #do something
    
#    #def getToolbarIcon(self):
#    #    return None

#    def getToolbarTip(self):
#        return "Type Facet Shortcuts"
        
#installTool(TypeFacetShortcuts2())
