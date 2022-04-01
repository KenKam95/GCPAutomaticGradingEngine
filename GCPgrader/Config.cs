using Google.Apis.Auth.OAuth2;
using Google.Apis.CloudResourceManager.v1;
using Google.Apis.CloudResourceManager.v1.Data;
using Google.Apis.Iam.v1;
using NUnit.Framework;

namespace GCPProjectGrader
{
    class Config
    {
        public Config()
        {

            var GCPAuthFilePath = TestContext.Parameters.Get("GCPCredentialsPath", null);
            var trace = TestContext.Parameters.Get("trace", null);
            TestContext.Out.WriteLine(trace);
            Credentials = SdkContext.GCPCredentialsFactory.FromFile(GCPAuthFilePath);
            SubscriptionId = Credentials.DefaultSubscriptionId;
        }
        public GCPCredentials Credentials { get; private set; }
        public string SubscriptionId { get; private set; }
    }
}