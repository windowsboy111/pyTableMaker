/*

Fader.js

Facilitates fading transition effects

Created by Kate Morley - http://code.iamkate.com/ - and released under the terms
of the CC0 1.0 Universal legal code:

http://creativecommons.org/publicdomain/zero/1.0/legalcode

*/

/* Creates a Fader. A Fader fades between a set of panels (the children of a
 * specific DOM node), initially showing the first panel. The parameters are:
 *
 * node     - either the DOM node containing the panels or the ID of the node
 * duration - the duration of fades, in seconds; this optional parameter
 *            defaults to 0.5
 */
function Fader(node, duration){

  // fetch the DOM node if a string was supplied
  if (typeof node == 'string') node = document.getElementById(node);

  // store the rate
  this.rate = 0.05 / (duration ? duration : 0.5);

  // style the node so that panels can be positioned on top of each other
  node.style.position = 'relative';

  // initialise the fader width and height
  var width  = 0;
  var height = 0;

  // initialise the list of panels
  this.panels = [];
  this.target = 0;

  // loop over the children of the node
  var child = node.firstChild;
  do{

    // check that this is an element node
    if (child.nodeType == 1){

      // update the fader width and height
      width  = Math.max(width,  child.offsetWidth);
      height = Math.max(height, child.offsetHeight);

      // position the panel
      child.style.position = 'absolute';
      child.style.top      = 0;
      child.style.left     = 0;

      // add this panel to the list of panels
      this.panels.push(
          {
            node    : child,
            opacity : (this.panels.length == 0 ? 1 : 0)
          });

    }

  }while (child = child.nextSibling);

  // set the fader width and height
  node.style.minWidth  = width  + 'px';
  node.style.minHeight = height + 'px';

  // determine whether the opacity or filter properties should be used
  this.useOpacity = 'opacity' in document.documentElement.style;

  // initialise the fader
  this.setTarget(0);

  // update the opacity ever 50 milliseconds
  var thisObject = this;
  window.setInterval(
      function(){
        thisObject.setPanelOpacity(
            thisObject.target,
            thisObject.panels[thisObject.target].opacity + thisObject.rate);
      },
      50);

}

/* Sets the target of the fader. The parameter is:
 *
 * target - the index of the new target panel
 */
Fader.prototype.setTarget = function(target){

  // clear any current timeout
  if ('timeout' in this) window.clearTimeout(this.timeout);

  // set the contribution from the current target panel
  this.panels[this.target].contribution = this.panels[this.target].opacity;

  // initialise the remaining contribution
  var remaining = 1 - this.panels[this.target].opacity;

  // loop over the other panels
  for (var index = 0; index < this.panels.length; index ++){
    if (index != this.target){

      // set the contribution of the panel and update the remaining contribution
      this.panels[index].contribution = remaining * this.panels[index].opacity;
      remaining *= (1 - this.panels[index].opacity);

    }
  }

  // set the opacity and z-index of the new target
  this.setPanelOpacity(target, this.panels[target].contribution);
  this.panels[target].node.style.zIndex  = this.panels.length;

  // initialise the remaining contribution
  remaining = 1 - this.panels[target].opacity;

  // loop over the other panels
  var zIndex = this.panels.length;
  for (var index = 0; index < this.panels.length; index ++){
    if (index != target){

      // set the opacity of the panel and update the remaining contribution
      this.setPanelOpacity(index, this.panels[index].contribution / remaining);
      remaining -= this.panels[index].contribution;

      // set the z-index of the panel
      zIndex --;
      this.panels[index].node.style.zIndex = zIndex;

    }
  }

  // store the new target
  this.target = target;

  // call the listener and reinstate the timeout if necessary
  if ('timeout' in this){
    if (this.listener) this.listener();
    this.setInterval(this.interval, null, this.listener);
  }

}

/* Sets the opacity of the specified panel. The parameters are:
 *
 * index   - the index of the panel
 * opacity - the opacity
 */
Fader.prototype.setPanelOpacity = function(index, opacity){

  // correct division by zero issues
  if (isNaN(opacity)) opacity = 0;

  // correct rounding issues
  opacity = Math.max(0, Math.min(1, opacity));

  // set the opacity of the panel
  this.panels[index].opacity = opacity;
  if (this.useOpacity){
    this.panels[index].node.style.opacity = opacity;
  }else{
    this.panels[index].node.style.filter  =
        'alpha(opacity=' + (100 * opacity) + ')';
  }

}

/* Sets the fader to cycle through its panels automatically. The parameters are:
 *
 * interval - the interval, in seconds, between changes of the target
 * delay    - the delay, in seconds, before the first change of target; this
 *            optional parameter defaults to the value of the interval parameter
 * listener - a function to call each time the target changes; this parameter is
 *            optional.
 */
Fader.prototype.setInterval = function(interval, delay, listener){

  // store the interval and listener
  this.interval = interval;
  this.listener = listener;

  // change the target after the specified interval
  var thisObject = this;
  this.timeout =
      window.setTimeout(
          function(){
            thisObject.setTarget(
                (thisObject.target + 1) % thisObject.panels.length);
          },
          (delay ? delay : interval) * 1000);

}

// Stops the fader from cycling through its panels automatically.
Fader.prototype.clearInterval = function(){

  // clear any current timeout
  if ('timeout' in this){
    window.clearTimeout(this.timeout);
    delete this.timeout;
  }

}
