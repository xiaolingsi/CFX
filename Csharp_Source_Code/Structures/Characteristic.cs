using System;
using System.Collections.Generic;
using System.Text;

namespace CFX.Structures
{
    /// <summary>
    /// A singular characteristic that has been applied to a production unit
    /// </summary>
    public class Characteristic
    {
        /// <summary>
        /// The name of the characteristic
        /// </summary>
        public string Name
        {
            get;
            set;
        }

        /// <summary>
        /// The value of the characteristic
        /// </summary>
        public string Value
        {
            get;
            set;
        }
    }
}
