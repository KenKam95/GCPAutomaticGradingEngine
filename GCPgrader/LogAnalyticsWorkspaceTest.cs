using Google.Cloud.Monitoring.V3;
using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace GCPProjectGrader
{
    [Parallelizable(scope: ParallelScope.Children)]
    class LogAnalyticsWorkspaceTest
    {
        private MonitorManagementClient client;

        public LogAnalyticsWorkspaceTest()
        {
            Setup();
        }

        [SetUp]
        public void Setup()
        {
            var config = new Config();
            client = new MonitorManagementClient(config.Credentials, new HttpClient(), true);
            client.SubscriptionId = config.SubscriptionId;                    
        }

  
    }
}